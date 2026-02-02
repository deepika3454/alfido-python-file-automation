import os
import shutil
import csv


def main():
    
    print("Automation script started")

    
    try:
        with open("input.txt", "r") as f:
            data = f.read()
    except FileNotFoundError:
        print("input.txt not found")
        return

    
    try:
        with open("output.txt", "w") as f:
            f.write(data.upper())
        print("output.txt created successfully")
    except Exception as e:
        print("Error while writing output.txt:", e)
    


    try:
        with open("sample.csv", "r") as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader)  # skip header row

            record_count = 0
            for row in reader:
                record_count += 1

        # Write summary to a text file
        with open("csv_summary.txt", "w") as summary:
            summary.write(f"Total Records: {record_count}")

        print("CSV processing completed successfully")

    except FileNotFoundError:
        print("sample.csv not found")

    except Exception as e:
        print("Error while processing CSV:", e)
        

        # Step 4: Backup automation
    try:
        backup_folder = "backup"

        # Create backup folder if it doesn't exist
        if not os.path.exists(backup_folder):
            os.mkdir(backup_folder)
            print("Backup folder created")

        # Files to move
        files_to_backup = ["output.txt", "csv_summary.txt"]

        for file in files_to_backup:
          source_path = file
          destination_path = os.path.join(backup_folder, file)

          if os.path.exists(source_path):
            if os.path.exists(destination_path):
                os.remove(destination_path)  # delete old backup
            shutil.move(source_path, backup_folder)
            print(f"{file} backed up successfully")
          else:
            print(f"{file} already backed up or not generated")

    except Exception as e:
        print("Backup automation failed:", e)




if __name__ == "__main__":
    main()
