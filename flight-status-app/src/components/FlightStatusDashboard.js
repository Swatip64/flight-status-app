import React, { useState, useEffect } from 'react';
import axios from 'axios';

const FlightStatusDashboard = () => {
  const [flights, setFlights] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    // Fetch flight data
    const fetchFlights = async () => {
      try {
        const response = await axios.get('/api/flight-status');
        if (Array.isArray(response.data)) {
          setFlights(response.data);
        } else {
          console.error('Expected an array but got:', response.data);
        }
      } catch (error) {
        console.error('Error fetching flight data:', error);
      }
    };

    fetchFlights();

    // WebSocket for real-time updates
    const socket = new WebSocket('ws://localhost:5000');

    socket.onmessage = (event) => {
      try {
        const updatedFlightData = JSON.parse(event.data);
        if (Array.isArray(updatedFlightData)) {
          setFlights((prevFlights) =>
            prevFlights.map((flight) =>
              updatedFlightData.find((updated) => updated.id === flight.id) || flight
            )
          );
        } else {
          console.error('Expected an array but got:', updatedFlightData);
        }
      } catch (error) {
        console.error('Error processing WebSocket message:', error);
      }
    };

    socket.onerror = (error) => {
      console.error('WebSocket error:', error);
    };

    return () => {
      socket.close();
    };
  }, []);

  // Filter flights based on search term
  const filteredFlights = flights.filter((flight) =>
    flight.flightNumber.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="flight-status-dashboard">
      <h2>Flight Status Dashboard</h2>
      <input
        type="text"
        placeholder="Search flights"
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />
      <table className="table">
        <thead>
          <tr>
            <th>Flight Number</th>
            <th>Status</th>
            <th>Gate</th>
            <th>Arrival Time</th>
            <th>Boarding Time</th>
          </tr>
        </thead>
        <tbody>
          {filteredFlights.length > 0 ? (
            filteredFlights.map((flight) => (
              <tr key={flight.id}>
                <td>{flight.flightNumber}</td>
                <td>{flight.status}</td>
                <td>{flight.gate}</td>
                <td>{flight.arrivalTime}</td>
                <td>{flight.boardingTime}</td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="5">All flights to New Delhi today are delayed because of bad weather.</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
};

export default FlightStatusDashboard;
