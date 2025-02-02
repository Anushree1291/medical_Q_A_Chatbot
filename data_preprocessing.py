import os
import xml.etree.ElementTree as ET
import json

def parse_medquad_data(data_folder):
    qa_pairs = []

    for file_name in os.listdir(data_folder):
        file_path = os.path.join(data_folder, file_name)

        # Skip non-XML files
        if not file_name.endswith(".xml"):
            continue

        try:
            # Parse the XML file
            tree = ET.parse(file_path)
            root = tree.getroot()

            # Extract Q&A pairs
            qa_pairs_element = root.find("QAPairs")
            if qa_pairs_element is not None:
                for qa_pair in qa_pairs_element.findall("QAPair"):
                    question_element = qa_pair.find("Question")
                    answer_element = qa_pair.find("Answer")

                    # Safely get the text of question and answer
                    question = question_element.text.strip() if question_element is not None and question_element.text else None
                    answer = answer_element.text.strip() if answer_element is not None and answer_element.text else None

                    # Only append pairs with both question and answer
                    if question and answer:
                        qa_pairs.append((question, answer))
                    elif question:
                        print(f"Skipping Q&A pair with missing answer in file: {file_name}, Question: {question}")
                    else:
                        print(f"Skipping Q&A pair with missing question in file: {file_name}")

            else:
                print(f"No QAPairs found in file: {file_name}")

        except ET.ParseError as e:
            print(f"XML parsing error in file: {file_path}, error: {e}")
        except Exception as e:
            print(f"Error processing file: {file_path}, error: {e}")

    print(f"Total Q&A pairs extracted: {len(qa_pairs)}")
    return qa_pairs




if __name__ == "__main__":
    # Directory containing XML files
    data_dir = "./data"  
    output_file = "./qa_pairs.json"

    # Parse and preprocess
    print("Parsing XML files...")
    qa_data = parse_medquad_data(data_dir)
    print(f"Parsed {len(qa_data)} question-answer pairs.")

    # Save the processed data
    print(f"Saving processed data to {output_file}...")
    with open(output_file, "w") as f:
        json.dump(qa_data, f)
    print("Data saved successfully!")
