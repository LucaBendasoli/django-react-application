import React, { useEffect, useState } from "react";
import axios from "axios";
import CarList from "../components/CarList";

const CarPage = () => {
  const [cars, setCars] = useState([]);

  useEffect(() => {
    const fetchCars = async () => {
      const res = await axios.get("/api/cars/");
      setCars(res.data);
    };
    fetchCars();
  }, []);

  return <CarList cars={cars} />;
};

export default CarPage;
