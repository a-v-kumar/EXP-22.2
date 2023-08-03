import os

def generate_image_links(folder_path):
    # Initialize an empty list to store the image links
    image_links = []

    # Recursive function to traverse through the folder and its subfolders
    def traverse_folder(current_folder):
        for filename in os.listdir(current_folder):
            # Get the full path of the file/directory
            file_path = os.path.join(current_folder, filename)
            if os.path.isdir(file_path):
                # If the current item is a folder, recursively traverse it
                traverse_folder(file_path)
            elif os.path.isfile(file_path):
                # If the current item is a file with an image extension, add its link
                image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
                if any(file_path.lower().endswith(ext) for ext in image_extensions):
                    image_links.append(file_path)

    # Start traversing the given folder
    traverse_folder(folder_path)

    return image_links

def generate_readme(folder_name, image_links):
    # Generate the Markdown content
    readme_content = f"# Images from {folder_name}\n\n"
    
    # Add image links to the readme
    for image_link in image_links:
        image_name = os.path.basename(image_link)
        readme_content += f"![{image_name}]({image_link})\n\n"

    return readme_content

if __name__ == "__main__":
    folder_name = "images"  # Replace this with the folder name you want to display
    image_links = generate_image_links(folder_name)
    readme_content = generate_readme(folder_name, image_links)

    # Write the content to the README.md file
    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)

