# laboratoryIS
# Laboratory Information System - User Module

Welcome to the **Laboratory Information System** repository! This repository contains Python files that form the user module for a laboratory information system. This module allows you to manage users within the system, including adding, removing, and updating user information.

## Table of Contents

- [Project Description](#project-description)
- [File Structure](#file-structure)
- [Usage](#usage)

## Project Description

The **Medical Laboratory System - User Module** is designed to help manage users in a medical laboratory system. It provides functionalities to define users, set passwords, remove users, list users, reset passwords, and change user names. This module is essential for maintaining user data and ensuring secure access to the system.

## File Structure

Here's an overview of the file structure in this repository:


- `README.md`: This file, providing an overview and instructions for the project.
- `main.py`: The main script that provides a menu-driven interface for managing users.
- `user.py`: Defines the `User` class, which encapsulates user information and functionalities.
- `user_file_manager.py`: Manages the persistence of user data using SQLite.
- `users.db`: to see the list of users, you can run: ``` SELECT * FROM users; ```

## Usage

Once you run the main.py script, you will see a menu with the following options:

0: Exit

1: Define User

2: Set password for user

3: Remove User

4: Get Users list

5: Reset User Password

6: Change User Name

Choose an option by entering the corresponding number and follow the prompts to manage users.
