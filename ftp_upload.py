import os
from ftplib import FTP, error_perm
from config import FTP_HOST, FTP_PORT, FTP_USER, FTP_PASS, DIRECTORY_PATH


def connect_ftp():
    ftp = FTP()
    try:
        print(f"Connecting to {FTP_HOST}:{FTP_PORT}")
        ftp.connect(FTP_HOST, FTP_PORT, timeout=60)  # Increased timeout to 60 seconds
        ftp.login(user=FTP_USER, passwd=FTP_PASS)
        print("Connected and logged in.")
        return ftp
    except Exception as e:
        print(f"Failed to connect or log in: {e}")
        exit(1)


def place_files(ftp, path):
    for name in os.listdir(path):
        localpath = os.path.join(path, name)
        if os.path.isfile(localpath):
            print("STOR", name, localpath)
            try:
                with open(localpath, 'rb') as file:
                    ftp.storbinary('STOR ' + name, file)
            except error_perm as e:
                print(f"Skipping file {name}: {e}")
        elif os.path.isdir(localpath):
            print("MKD", name)
            try:
                ftp.mkd(name)
            except error_perm as e:
                if not e.args[0].startswith('550'):
                    print(f"Error creating directory {name}: {e}")
                    raise
            try:
                print("CWD", name)
                ftp.cwd(name)
                place_files(ftp, localpath)
                print("CWD", '..')
                ftp.cwd('..')
            except error_perm as e:
                if not e.args[0].startswith('550'):
                    print(f"Error changing to directory {name}: {e}")
                    raise
                else:
                    print(f"Skipping directory {name}: {e}")


def main():
    ftp = connect_ftp()
    place_files(ftp, DIRECTORY_PATH)
    ftp.quit()


if __name__ == "__main__":
    main()
