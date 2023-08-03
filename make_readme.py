import os
from urllib.parse import quote

def generate_image_links(folder_path):
    # Initialize a dictionary to store image links for each image name
    image_links_dict = {}

    # Recursive function to traverse through the folder and its subfolders
    def traverse_folder(current_folder, base_path):
        for filename in os.listdir(current_folder):
            # Get the full path of the file/directory
            file_path = os.path.join(current_folder, filename)
            if os.path.isdir(file_path):
                # If the current item is a folder, recursively traverse it
                traverse_folder(file_path, base_path)
            elif os.path.isfile(file_path):
                # If the current item is a file with an image extension, add its link
                image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
                if any(file_path.lower().endswith(ext) for ext in image_extensions):
                    relative_image_path = os.path.relpath(file_path, base_path)
                    image_name = os.path.basename(file_path)
                    image_name_encoded = quote(image_name, safe="")  # Keep all characters including '%20'
                    if image_name not in image_links_dict:
                        image_links_dict[image_name] = []
                    image_links_dict[image_name].append((image_name_encoded, relative_image_path))

    # Start traversing the given folder
    traverse_folder(folder_path, folder_path)

    return image_links_dict

def generate_readme(folder_path, image_links_dict):
    # Generate the Markdown content for each image name and its images
    if image_links_dict:
        readme_content = ""

        for image_name, image_links in image_links_dict.items():
            readme_content += f"# {image_name}\n\n"

            # Add image links to the readme in rows of three
            num_images = len(image_links)
            for i in range(0, num_images, 3):
                row_images = image_links[i:i+3]
                row_content = " | ".join(f"[<img src='{img_link_rel}' width='200' />]({img_link_rel[:10]})" for img_name, img_link_rel in row_images)
                readme_content += row_content + "\n\n"

        # Write the content to the README.md file in the respective folder
        readme_file_path = os.path.join(folder_path, "README.md")
        with open(readme_file_path, "w") as readme_file:
            readme_file.write(readme_content)

if __name__ == "__main__":
    root_folder = "."  # Replace this with the name of your root folder
    for root, dirs, files in os.walk(root_folder):
        image_links_dict = generate_image_links(root)

        # Generate README.md file for the current folder
        generate_readme(root, image_links_dict)

