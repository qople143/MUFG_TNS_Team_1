"""
Template Manager Module
Handles saving and loading of operation templates.
"""

import json
import os
from typing import Dict, List, Optional
import logging

logger = logging.getLogger(__name__)


class TemplateManager:
    """
    Manages operation templates for reuse.
    
    Allows users to save and load transformation workflows.
    """
    
    def __init__(self, templates_dir: str = "templates"):
        """
        Initialize TemplateManager.
        
        Args:
            templates_dir: Directory to store template files
        """
        self.templates_dir = templates_dir
        self._ensure_templates_dir()
    
    def _ensure_templates_dir(self):
        """Create templates directory if it doesn't exist."""
        if not os.path.exists(self.templates_dir):
            os.makedirs(self.templates_dir)
            logger.info(f"Created templates directory: {self.templates_dir}")
    
    def save_template(self, name: str, operations: List[Dict]) -> bool:
        """
        Save operations as a template.
        
        Args:
            name: Template name
            operations: List of operation dictionaries
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            template_path = os.path.join(self.templates_dir, f"{name}.json")
            
            template_data = {
                'name': name,
                'operations': operations,
                'created_at': str(pd.Timestamp.now())
            }
            
            with open(template_path, 'w') as f:
                json.dump(template_data, f, indent=2)
            
            logger.info(f"Template '{name}' saved successfully")
            return True
            
        except Exception as e:
            logger.error(f"Error saving template: {str(e)}")
            return False
    
    def load_template(self, name: str) -> Optional[Dict]:
        """
        Load a template by name.
        
        Args:
            name: Template name
            
        Returns:
            Dict containing template data, or None if not found
        """
        try:
            template_path = os.path.join(self.templates_dir, f"{name}.json")
            
            if not os.path.exists(template_path):
                logger.warning(f"Template '{name}' not found")
                return None
            
            with open(template_path, 'r') as f:
                template_data = json.load(f)
            
            logger.info(f"Template '{name}' loaded successfully")
            return template_data
            
        except Exception as e:
            logger.error(f"Error loading template: {str(e)}")
            return None
    
    def list_templates(self) -> List[str]:
        """
        List all available templates.
        
        Returns:
            List of template names
        """
        try:
            if not os.path.exists(self.templates_dir):
                return []
            
            templates = [f.replace('.json', '') for f in os.listdir(self.templates_dir) 
                        if f.endswith('.json')]
            
            return sorted(templates)
            
        except Exception as e:
            logger.error(f"Error listing templates: {str(e)}")
            return []
    
    def delete_template(self, name: str) -> bool:
        """
        Delete a template.
        
        Args:
            name: Template name
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            template_path = os.path.join(self.templates_dir, f"{name}.json")
            
            if os.path.exists(template_path):
                os.remove(template_path)
                logger.info(f"Template '{name}' deleted successfully")
                return True
            else:
                logger.warning(f"Template '{name}' not found")
                return False
                
        except Exception as e:
            logger.error(f"Error deleting template: {str(e)}")
            return False


# Import pandas for timestamp
import pandas as pd
