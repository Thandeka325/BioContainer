import React, { useEffect, useState } from "react";
import axios from "axios";

const UserDashboard = () => {
  const [user, setUser] = useState(null);
  const [containers, setContainers] = useState([]);

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        // Fetch user profile
        const userResponse = await axios.get(
          `${process.env.REACT_APP_API_URL}/api/user-profile`,
          {
            headers: { Authorization: `Bearer ${localStorage.getItem("token")}` }
          }
        );
        setUser(userResponse.data);
      } catch (error) {
        console.error("Error fetching user profile:", error);
      }
    };

    const fetchUserContainers = async () => {
      try {
        // Fetch past containers
        const containersResponse = await axios.get(
          `${process.env.REACT_APP_API_URL}/api/user-containers`,
          {
            headers: { Authorization: `Bearer ${localStorage.getItem("token")}` }
          }
        );
        setContainers(containersResponse.data);
      } catch (error) {
        console.error("Error fetching containers:", error);
      }
    };

    fetchUserData();
    fetchUserContainers();
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
        <p>Loading user data...</p>
      )}

      <h3>Past Container Generations</h3>
      {containers.length > 0 ? (
        <ul>
          {containers.map((container) => (
            <li key={container.id}>
              <strong>Container ID:</strong> {container.id} - 
              <strong>Status:</strong> {container.status}
            </li>
          ))}
        </ul>
      ) : (
        <p>No past container generations found.</p>
      )}
    </div>
  );
};

export default UserDashboard;
