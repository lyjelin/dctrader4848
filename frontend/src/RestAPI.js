import axios from "axios";
import React, { useState } from "react";
import "./RestAPI.css";

function RestAPI() {
  const [order, setOrder] = useState([]);

  return (
    <>
      <h1>REST API 연습</h1>
      <div className="btn-primary">
        <button
          onClick={() => {
            axios
              .post("http://127.0.0.1:8000/order/", {
                orderID: "주문번호",
                orderItem: "dummy",
                orderBudget: 816
              })
              .then(function (response) {
                console.log(response);
              })
              .catch(function (error) {
                console.log(error);
              });
          }}
        >
          POST
        </button>
        <button
          onClick={() => {
            axios
              .get("http://127.0.0.1:8000/order/")
              .then((response) => {
                setOrder([...response.data]);
                console.log(response.data);
              })
              .catch(function (error) {
                console.log(error);
              });
          }}
        >
          GET
        </button>
      </div>
      {order.map((e) => (
        <div>
          {" "}
          <div className="list">
            <span>
              {e.id}번, {e.orderID}, {e.orderItem}, {e.orderDate}
            </span>
            <button
              className="btn-delete"
              onClick={() => {
                axios.delete(`http://127.0.0.1:8000/order/${e.id}`);
                setOrder(order.filter((order) => order.id !== e.id));
              }}
            >
              DELETE
            </button>{" "}
          </div>
        </div>
      ))}
    </>
  );
}

export default RestAPI;