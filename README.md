# MultiLanguage Invoice Extractor

This application is a MultiLanguage Invoice Extractor that allows you to extract information from invoices in various languages. You can run this application both locally on a Windows machine and on an AWS EC2 instance.

## Running Locally on Windows:

### Prerequisites:
- Anaconda installed on your local machine.
- Clone of the `google-gemini` repository.

### Steps:
1. Open Anaconda Command Prompt.
2. Navigate to the `google-gemini` directory.
3. Create a new Anaconda environment:
   ```bash
   conda create -n google-gemini python=3.11 -y
   ```
4. Activate the environment:
   ```bash
   conda activate google-gemini
   ```
5. Install the required Python packages:
   ```bash
   pip install -r requirement.txt
   ```
6. Create a `.env` file in the `google-gemini` directory and add your Google API key:
   ```plaintext
   GOOGLE_API_KEY="<Supply your secret token here>"
   ```
7. Run the MultiLanguage Invoice Extractor using Streamlit:
   ```bash
   streamlit run app.py --server.port 8080
   ```
8. Access the application on http://localhost:8080 from your web browser.
9. Upload an invoice file and ask any question to extract information.

## Running on AWS EC2:

### Prerequisites:
- An AWS account.
- Basic knowledge of setting up and accessing an EC2 instance.

### Steps:
1. Launch an EC2 instance with Ubuntu.
2. SSH into the EC2 instance.
3. Update the OS and install necessary packages:
   ```bash
   sudo apt update
   sudo apt-get update
   sudo apt upgrade -y
   sudo apt install git curl unzip tar make sudo vim wget python3-pip -y
   ```
4. Clone the `google-gemini` repository:
   ```bash
   git clone git@github.com:ThirdEyeInfo/google-gemini.git
   cd google-gemini
   ```
5. Install the required Python packages:
   ```bash
   pip3 install -r requirement.txt
   ```
6. Add your Google API key in the `.env` file:
   ```bash
   vi .env
   ```
   Add the following line, then save and exit:
   ```plaintext
   GOOGLE_API_KEY="<Supply your secret token here>"
   ```
7. Run the MultiLanguage Invoice Extractor using Streamlit:
   ```bash
   python3 -m streamlit run app.py --server.port 8080
   ```
8. Make port 8080 accessible from the public domain by configuring the EC2 instance's security group.
9. Access the application using the Public IPv4 address of the EC2 instance.

## Author
Dhiraj Chaudhari

LinkedIn: [Dhiraj Chaudhari](https://www.linkedin.com/in/dhiraj-chaudhari-06ba10259/)
