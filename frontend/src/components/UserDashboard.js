import React, { useEffect, useState } from "react";
import axios from "axios";

const UserDashboard = () => {
  const [user, setUser] = useState(null);
  const [containers, setContainers] = useState([]);

  useEffect(() => {
    // Fetch user profile
    axios.get("https://biocontainer-api.onrender.com/api/user-profile", {
      headers: { Authorization: `Bearer ${localStorage.getItem("token")}` }
    })
    .then((response) => setUser(response.data))
    .catch((error) => console.error("Error fetching user profile:", error));

    // Fetch past containers
    axios.get("https://biocontainer-api.onrender.com/api/user-containers", {
      headers: { Authorization: `Bearer ${localStorage.getItem("token")}` }
    })
    .then((response) => setContainers(response.data))
    .catch((error) => console.error("Error fetching containers:", error));
  }, []);

  return (
    <div className="dashboard">
      <h2>User Dashboard</h2>

      {user ? (
        <div>
          <p><strong>Username:</strong> {user.username}</p>
          <p><strong>Email:</strong> {user.email}</p>
        </div>
      ) : (
        <p>Loading user profile...</p>
      )}

      <h3>Past Containers</h3>
      {containers.length > 0 ? (
        <ul>
          {containers.map((container) => (
            <li key={container.id}>
              <strong>{container.name}</strong> - {container.software} (Created: {new Date(container.created_at).toLocaleDateString()})
            </li>
          ))}
        </ul>
      ) : (
        <p>No containers created yet.</p>
      )}
    </div>
  );
};

export default UserDashboard;
