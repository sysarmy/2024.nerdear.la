import xml.etree.ElementTree as ET
import sys
import os

def transform_svg(input_file):
    try:
        # Parse the original SVG file
        tree = ET.parse(input_file)
        root = tree.getroot()
        
        # Extract viewBox attributes
        viewBox = root.attrib.get('viewBox', None)
        if viewBox:
            x, y, width, height = map(float, viewBox.split())
        else:
            width = float(root.attrib.get('width', 0))
            height = float(root.attrib.get('height', 0))
        
        if not width or not height:
            print("Cannot determine original viewBox or dimensions.")
            return

        # Calculate the new position to center the original content
        dx = (450 - width) / 2
        dy = (450 - height) / 2

        # Update viewBox attribute for the root
        root.attrib['viewBox'] = f"0 0 450 450"

        # Translate original content to center it in the new viewBox
        for elem in root:
            transform = elem.attrib.get('transform', '')
            new_transform = f"translate({dx}, {dy}) {transform}"
            elem.attrib['transform'] = new_transform.strip()
        
        # Write the new SVG into the 'square' directory
        output_file = os.path.join('square', os.path.basename(input_file))
        tree.write(output_file)
        print(f"Transformed SVG saved to {output_file}")

    except ET.ParseError as e:
        print(f"Error parsing SVG: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script_name.py input_file.svg")
    else:
        transform_svg(sys.argv[1])

