import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Chart from 'react-apexcharts';

function App() {
  const [spikes, setSpikes] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/dashboard-data')
      .then(res => setSpikes(res.data.spikes.spikes))
      .catch(err => console.error(err));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>BTC Volume Spike Dashboard</h1>
      <pre>{JSON.stringify(spikes, null, 2)}</pre>
    </div>
  );
}

export default App;
