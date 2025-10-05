# 🎟️ Event Management API  
**Backend Engineering Capstone Project (Django + Django REST Framework)**  

## 📘 Project Overview  
The **Event Management API** is a Django-based backend system that allows users to **create, manage, and explore events**. Built with Django REST Framework (DRF), this project simulates real-world event management platforms, focusing on robust CRUD operations, user authentication, and role-based permissions.  

Users can:  
- Create, update, and delete their own events.  
- Browse upcoming events with filtering and pagination.  
- Manage event capacity and prevent overbooking.  
- (Optionally) Register for events, leave feedback, or subscribe to notifications.  

---

## ⚙️ Functional Requirements  

### 🗓️ Event Management (CRUD)
- Create, Read, Update, and Delete (CRUD) events.  
- Each event includes:  
  - **Title**  
  - **Description**  
  - **Date & Time**  
  - **Location**  
  - **Organizer (User)**  
  - **Capacity (max attendees)**  
  - **Created Date**  
- Validation:  
  - Prevent creation of events with **past dates**.  
  - Ensure **required fields** (Title, Date & Time, Location) are provided.  

### 👤 User Management (CRUD)
- Implement full CRUD for users.  
- Fields: **Username**, **Email**, and **Password**.  
- Users can **only manage events they created**.  
- Enforce **permission checks** for event ownership.  

### 🔍 View Upcoming Events
- Endpoint to list all **upcoming (future)** events.  
- Supports **filtering** by:  
  - Title  
  - Location  
  - Date Range  
- Includes **pagination** for performance on large datasets.  

### 🧮 Event Capacity Management
- Each event has a **maximum capacity**.  
- Prevent new registrations once capacity is reached.  
- *(Optional)* Implement **waitlist** functionality.  

---

## 🧠 Technical Requirements  

### 🗄️ Database
- Use **Django ORM** for database interactions.  
- Define models for `User` and `Event`.  
- Associate each event with its **creator (organizer)**.  

### 🔐 Authentication
- Use Django’s built-in authentication system.  
- Only **authenticated users** can create, update, or delete events.  
- *(Optional)* Add **JWT Authentication** for enhanced API security.  

### 🌐 API Design
- Built with **Django REST Framework (DRF)**.  
- Follows **RESTful design principles**.  
- Supports HTTP methods: `GET`, `POST`, `PUT`, `DELETE`.  
- Proper error handling with relevant HTTP status codes:  
  - `400` – Bad Request  
  - `401` – Unauthorized  
  - `403` – Forbidden  
  - `404` – Not Found  

### 🚀 Deployment
- Deploy on **Heroku** or **PythonAnywhere**.  
- Ensure the deployed API is **secure, performant, and accessible**.  

---

## 🧩 Stretch Goals (Optional Features)

| Feature | Description |
|----------|--------------|
| 📝 **Event Registration** | Allow users to register for events, decrementing capacity dynamically. |
| 🏷️ **Event Categories** | Add categories (e.g., Workshop, Concert) and allow filtering by category. |
| 🔔 **Notifications** | Send alerts (email or in-app) when event dates are approaching. |
| 💬 **Comments & Feedback** | Enable users to leave feedback on past events. |
| 📅 **Calendar Integration** | Integrate with Google Calendar or iCal for easy reminders. |
| ♻️ **Recurring Events** | Support for repeating events (weekly, monthly, etc.). |

---

