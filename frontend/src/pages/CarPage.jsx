import React, { useEffect, useState } from "react";
import CarList from "../components/CarList";
import LoadingIndicator from "../components/LoadingIndicator";
import api from "../api";

const CarPage = () => {
  const [cars, setCars] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    api
      .get("/api/cars/")
      .then((res) => {
        setCars(res.data);
        setLoading(false);
      })
      .catch((err) => {
        alert(`Error fetching cars: ${err}`);
        setError(error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <LoadingIndicator />;
  }

  if (error) {
    return alert(`Error loading cars: ${error}`);
  }

  return (
    <div>
      <h1>Car List</h1>
      <CarList cars={cars} />
    </div>
  );
};

export default CarPage;
