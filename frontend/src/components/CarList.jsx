import React from "react";

const CarList = ({ cars }) => {
  if (!Array.isArray(cars) | cars.length === 0) {
    return <div>No cars available.</div>
  }

  return (
    <div>
      {cars.map((car) => (
        <div key={car.id}>
          <h2>
            {car.make} {car.model}
          </h2>
          <p>Color: {car.color}</p>
          <p>Year: {car.year}</p>
          <p>Mileage: {car.mileage}</p>
          <p>Price: {car.price}</p>
          <p>Fuel Type: {car.fuel_type}</p>
          {car.image && (
            <img src={car.image} alt={`${car.make} ${car.model}`} />
          )}
        </div>
      ))}
    </div>
  );
};

export default CarList;
