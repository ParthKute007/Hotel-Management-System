## Problem Statement

Small restaurants and cafes often struggle with manual table management, order tracking, and billing processes. This leads to several challenges:

- Difficulty in tracking which tables are occupied or available
- Manual calculation errors in billing
- Time-consuming order documentation
- Lack of organized record-keeping for customer orders
- Inefficient table turnover due to poor tracking
- Paper waste from handwritten bills

There is a need for a simple, automated system that can streamline restaurant operations without requiring expensive software or complex training.

## Scope of the Project

The Hotel Management System is designed to automate basic restaurant operations through a console-based application. The project scope includes:

**In Scope:**
- Management of up to 10 tables with real-time availability tracking
- Digital menu with 17 pre-defined food and beverage items
- Automated order-taking process with quantity specification
- Automatic bill calculation and generation
- Bill storage as text files for record-keeping
- Table status management (occupied/free)
- Simple user interface requiring no technical expertise

**Out of Scope:**
- Database integration for long-term data storage
- Multi-restaurant support
- Employee/waiter management
- Inventory tracking
- Customer relationship management (CRM)
- Online ordering or delivery integration
- Payment gateway integration
- Graphical user interface (GUI)
- Menu customization by users
- Tax/GST calculations

## Target Users

This system is designed for:

### Primary Users:
1. **Small Restaurant Owners**: Independent restaurant owners looking for a cost-effective solution to manage daily operations
2. **Cafe Managers**: Cafe operators needing simple table and order management
3. **Food Court Vendors**: Small food stalls requiring basic billing and order tracking

### Secondary Users:
1. **Students**: Computer science students learning Python and basic software development
2. **Startup Restaurants**: New restaurant ventures with limited budgets for expensive POS systems
3. **Training Institutes**: Educational institutions teaching restaurant management basics

### User Characteristics:
- Basic computer literacy required
- No technical background needed
- Comfortable with keyboard input
- Need quick, reliable billing system
- Operate small to medium-sized establishments (up to 10 tables)

## High-Level Features

### 1. Table Allocation System
- Automatic assignment of available tables to customers
- Real-time tracking of table occupancy status
- Notification when no tables are available
- Table release after payment confirmation

### 2. Menu Management
- Pre-loaded menu with 17 items across multiple categories
- Items include pizzas, snacks, main courses, beverages, and desserts
- Price display for all menu items
- Quick menu browsing for customers

### 3. Order Processing
- Interactive order placement system
- Multiple item ordering in a single transaction
- Quantity specification for each item
- Input validation to prevent invalid orders
- Case-insensitive item name recognition

### 4. Billing System
- Automatic calculation of order totals
- Individual bill generation for each table
- Itemized bill breakdown showing quantities and amounts
- Bill storage as text files for records
- File naming convention: `bill_table_X.txt`

### 5. Payment Management
- Payment confirmation tracking
- Automatic table release upon payment
- Visual feedback on successful payment processing

### 6. User Interface
- Simple text-based interface
- Clear prompts and instructions
- Easy navigation with keywords ('start', 'done', 'exit')
- Error messages for invalid inputs
- Confirmation messages for completed actions

### 7. Data Persistence
- Bill files saved locally for future reference
- Organized file storage by table number
- Easy retrieval of transaction history