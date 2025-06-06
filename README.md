# Streamlit Wiki App 🚀

![Streamlit Wiki App](https://img.shields.io/badge/Streamlit%20Wiki%20App-v1.0-blue)

Welcome to the **Streamlit Wiki App**! This project serves as an end-to-end implementation of a Text to Math Problem Solver. Utilizing the powerful Google Gemma 2 language model via LangChain Groq, this app combines advanced natural language processing and reasoning capabilities to understand, solve, and explain mathematical problems in a clear, step-by-step manner. Additionally, the app integrates Wikipedia search functionality to enhance user experience and provide context to the problems being solved.

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)
7. [Contact](#contact)
8. [Releases](#releases)

## Features

- **Text to Math Problem Solving**: Convert natural language questions into mathematical problems.
- **Step-by-Step Solutions**: Understand the reasoning behind each solution.
- **Wikipedia Integration**: Access relevant Wikipedia articles for additional context.
- **User-Friendly Interface**: Built using Streamlit for an intuitive user experience.
- **Open Source**: Free to use and modify.

## Technologies Used

- **Streamlit**: A powerful framework for building web apps with Python.
- **Google Gemma 2**: Advanced language model for natural language understanding.
- **LangChain**: Framework for building applications with language models.
- **Wikipedia API**: For fetching articles and information.
- **Python**: The programming language used for development.
- **Docker**: For containerization and easy deployment.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/MajkSK21/streamlit-wiki-app.git
   cd streamlit-wiki-app
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   streamlit run app.py
   ```

## Usage

After launching the app, you will see a user-friendly interface where you can input your mathematical questions in natural language. 

1. Type your question into the input box.
2. Click on the "Solve" button.
3. The app will process your request using the Google Gemma 2 model and provide a step-by-step solution.
4. If relevant, you can also access related Wikipedia articles directly from the app.

## Contributing

We welcome contributions! If you would like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or suggestions, feel free to reach out:

- **Email**: your-email@example.com
- **GitHub**: [MajkSK21](https://github.com/MajkSK21)

## Releases

You can find the latest releases of the Streamlit Wiki App [here](https://github.com/MajkSK21/streamlit-wiki-app/releases). Make sure to download and execute the latest version for the best experience.

If you encounter any issues, please check the "Releases" section for updates or troubleshooting.

---

Thank you for checking out the Streamlit Wiki App! We hope you find it useful for solving your mathematical queries. Happy solving!