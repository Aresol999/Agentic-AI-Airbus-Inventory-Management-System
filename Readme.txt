AGENTIC AI AIRBUS INVENTORY MANAGEMENT SYSTEM
A backend-focused, agent-enabled inventory management system built using Python, MySQL, and the Model Context Protocol (MCP). The project demonstrates how a structured database-backed system can be exposed as an intelligent tool-driven agent and connected to desktop AI clients such as Claude Desktop. The system simulates a real-world Airbus inventory workflow with querying, updates, and analytics handled through MCP tools.

--------------------------------------------------------------------------------------

PROJECT OVERVIEW

This project models an Airbus inventory management platform where inventory data is stored in a MySQL database and accessed through an MCP server written in Python. The MCP server exposes structured tools that allow an AI client to retrieve, insert, update, and manage inventory records in a controlled and auditable manner.

The application follows a clean separation between database configuration, business logic, and MCP tool definitions, demonstrating real-world backend and agentic AI design patterns.

--------------------------------------------------------------------------------------

INSTALLATION & RUN INSTRUCTIONS

Prerequisites:
• Python 3.10+ installed
• MySQL Server installed and running
• Claude Desktop (or any MCP-compatible client)
• pip installed

Steps to Run the Project:

1. Clone the repository/download ZIP

2. Open the project folder in a terminal

3. Install required dependencies by running:
   pip install -r requirements.txt

4. Ensure MySQL credentials are correctly configured in the server file

5. Start the MCP server using:
   python server.py

6. Configure the MCP server in Claude Desktop using the below JSON configuration

{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "C:/Users/arnav/OneDrive/Desktop"
      ]
    },
    "airbus-inventory": {
      "command": "C:/Python313/python.exe",
      "args": [
        "D:/University/Projects/GenAI - MCP with mySQLconnector Project/server.py"
      ],
      "cwd": "D:/University/Projects/GenAI - MCP with mySQLconnector Project"
    }
  }
}

7. Restart Claude Desktop


--------------------------------------------------------------------------------------

TECHNOLOGY STACK

Backend:
• Python
• Model Context Protocol (MCP – FastMCP)
• MySQL

Database:
• MySQL (Relational schema for inventory, products, and transactions)

Tools & Libraries:
• pymysql / mysql-connector
• contextlib (for connection handling)
• Claude Desktop MCP integration

--------------------------------------------------------------------------------------

CORE FUNCTIONALITIES

• Inventory creation and initialization
• Add, update, delete, and query Airbus inventory items
• Structured MCP tools for database operations
• Persistent MySQL-backed data storage
• Safe database connection handling using context managers
• AI-agent interaction via MCP tool calls

--------------------------------------------------------------------------------------

LEARNING OUTCOMES

• Hands-on experience building MCP servers in Python
• Practical understanding of agentic AI tool design
• Integration of MySQL with AI-driven workflows
• Clean backend architecture with database abstraction
• Exposure to real-world enterprise inventory system patterns
• Understanding how LLM clients interact with structured backend tools

--------------------------------------------------------------------------------------

IMPROVEMENTS

• REST API layer in parallel with MCP tools
• Cloud database deployment
• Production-grade logging and monitoring
• Integration with ERP or supply chain systems

--------------------------------------------------------------------------------------

AUTHOR

Arnav Kadyan

