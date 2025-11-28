# Hotel-Management-System
This is a console-based Python application that automates restaurant operations including table allocation order processing, and  billing. The system manages up to 10 tables, processes orders from a 17-item  menu, and generates itemized bills automatically. It eliminates manual errors,  improves efficiency, and maintains digital transaction records
# Hotel Management System

## Overview

A Python-based restaurant management system that handles table bookings, order processing, and bill generation. This console application automates the workflow of a small restaurant by managing table allocation, taking customer orders from a menu, calculating bills, and tracking table availability.

## Features

- Automatic table allocation system (manages 10 tables)
- Interactive menu with 17 food and beverage items
- Order placement with quantity tracking
- Automatic bill generation and file storage
- Table status management (occupied/free)
- Real-time total calculation
- Payment confirmation tracking

## Technologies/Tools Used

- **Programming Language**: Python 
- **Built-in Libraries**: 
  - File I/O operations (no external dependencies)
- **Data Structures**: 
  - Lists for table management
  - Dictionaries for menu storage

## Steps to Install & Run the Project

1. **Prerequisites**: Ensure Python 3.x is installed on your system
   ```bash
   python --version
   ```

2. **Download the file**: Save the `hotel_management.py` file to your local directory

3. **Navigate to the directory**:
   ```bash
   cd path/to/your/directory
   ```

4. **Run the program**:
   ```bash
   python hotel_management.py
   ```

## Instructions for Testing

### Test Case 1: Normal Order Flow
1. Run the program
2. Type `start` when prompted
3. Note the assigned table number
4. Order items from the menu:
   - Enter: `farmhouse pizza`
   - Enter quantity: `2`
   - Enter: `coffee`
   - Enter quantity: `1`
   - Type: `done`
5. Verify bill is generated with correct total (₹320)
6. Type `yes` when asked about payment
7. Verify table is freed

### Test Case 2: Invalid Item Handling
1. Start a new order
2. Enter an item not in the menu (e.g., `burger`)
3. Verify error message appears
4. Continue ordering valid items

### Test Case 3: Table Capacity
1. Run the program and create 10 orders (don't mark as paid)
2. Try to start an 11th order
3. Verify "no table available" message appears

### Test Case 4: Empty Order
1. Start an order
2. Type `done` immediately without ordering anything
3. Verify system handles it gracefully

### Test Case 5: Exit Functionality
1. Type `exit` at the start prompt
2. Verify program terminates properly

### Expected Output Files
- Check for `bill_table_X.txt` files in the directory
- Open and verify bill format and calculations.

- 


