# import modules
import os
import shutil


class MainApp:
    def __init__(self, main_dir, secondary_dir, copied_dir):
        self.main_dir = main_dir
        self.secondary_dir = secondary_dir
        self.copied_dir = copied_dir

    def start(self):

        try:
            # Get the list of all files and directories
            files = os.listdir(self.main_dir)

            # Filtering only the files.
            files = [f for f in files if os.path.isfile(self.main_dir + '/' + f)]
            print(*files, sep="\n")

            for file in files:
                if file in os.listdir(self.secondary_dir):
                    source = f"{self.secondary_dir}\\{str(file)}"
                    dest = f"{self.copied_dir}\\{str(file)}"
                    shutil.copyfile(source, dest)
            print("All duplicate files copied successfully")

        except FileNotFoundError:
            print("Please Enter a valid directory! ")

        except Exception as e:
            print(e)


# asking user about the directory
main_dir = input("Enter the main directory: ")
secondary_dir = input("Enter the secondary directory: ")
copied_dir = input("Enter the copied directory: ")


if __name__ == '__main__':
    a = MainApp(main_dir, secondary_dir, copied_dir)
    a.start()
