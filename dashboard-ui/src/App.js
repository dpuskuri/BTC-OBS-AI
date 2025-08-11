import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Chart from 'react-apexcharts';

function App() {
  const [spikes, setSpikes] = useState([]);

  useEffect(() => {
    axios.get('/dashboard-data')
      .then(res => setSpikes(res.data.spikes));
  }, []);

  return (
    <div>
      <h1>BTC Volume Spikes</h1>
      {/* render spikes using your chart lib */}
      {/* Example: <Chart options={...} series={...} /> */}
      {/* ... */}
    </div>
  );
}

export default App;
