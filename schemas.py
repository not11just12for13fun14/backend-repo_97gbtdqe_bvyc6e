"""
Database Schemas for Kochi Metro Rail Limited website

Each Pydantic model represents a MongoDB collection. The collection name is the
lowercase of the class name.
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal
from datetime import datetime

class Alert(BaseModel):
    """
    Service alerts displayed on the website
    Collection: "alert"
    """
    title: str = Field(..., description="Short headline for the alert")
    message: str = Field(..., description="Detailed description")
    severity: Literal["info", "warning", "critical"] = Field("info", description="Type of alert")
    active: bool = Field(True, description="Whether the alert is currently active")
    start_time: Optional[datetime] = Field(None, description="When the alert starts")
    end_time: Optional[datetime] = Field(None, description="When the alert ends")

class Feedback(BaseModel):
    """
    Passenger feedback and contact submissions
    Collection: "feedback"
    """
    name: str = Field(..., description="Passenger name")
    email: Optional[EmailStr] = Field(None, description="Contact email")
    subject: str = Field(..., description="Topic of the message")
    message: str = Field(..., description="Feedback message")
    category: Literal["compliment", "suggestion", "issue", "other"] = Field("other")
    station: Optional[str] = Field(None, description="Station this relates to, if any")

# You can add more schemas as the site grows, e.g., Events, LostAndFound, etc.
