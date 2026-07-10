"""
Database management for CryptoMatrix
SQLite database wrapper and utilities
"""

import sqlite3
from pathlib import Path
from typing import Optional, List, Dict, Any
from core.config import DATABASE_PATH
from core.logger import setup_logger


logger = setup_logger(__name__)


class Database:
    """Database connection and query management"""
    
    def __init__(self, db_path: Path = DATABASE_PATH):
        """
        Initialize database connection
        
        Args:
            db_path: Path to SQLite database file
        """
        self.db_path = db_path
        self.connection: Optional[sqlite3.Connection] = None
    
    def connect(self):
        """Establish database connection"""
        try:
            self.connection = sqlite3.connect(str(self.db_path))
            self.connection.row_factory = sqlite3.Row
            logger.info(f"Connected to database: {self.db_path}")
        except sqlite3.Error as e:
            logger.error(f"Database connection error: {e}")
            raise
    
    def disconnect(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()
            logger.info("Database connection closed")
    
    def execute(self, query: str, params: tuple = ()) -> sqlite3.Cursor:
        """
        Execute a SQL query
        
        Args:
            query: SQL query string
            params: Query parameters
        
        Returns:
            Cursor object
        """
        if not self.connection:
            raise RuntimeError("Database not connected")
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            return cursor
        except sqlite3.Error as e:
            logger.error(f"Query execution error: {e}")
            raise
    
    def commit(self):
        """Commit pending transactions"""
        if self.connection:
            self.connection.commit()
            logger.debug("Database changes committed")
    
    def init_tables(self):
        """Initialize database schema"""
        logger.info("Initializing database schema")
        # Add table creation queries as needed
        # This is a placeholder for future schema setup


# Global database instance
db = Database()
