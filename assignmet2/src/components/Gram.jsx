import React, { useState } from "react";

export default function Gram() {
  const [post, setPost] = useState([]);
  const [name, setName] = useState("");
  const [cap, setCap] = useState("");

  const submit = () => {
    let obj = {
      name,
      cap,
    };
    setPost([...obj, post]);
    console.log(post);
  };

  return (
    <div>
      <nav>
        <img
          width={"20%"}
          src="https://www.shutterstock.com/image-vector/zdolbuniv-ukraine-march-29-2023-260nw-2281736183.jpg"
        />
      </nav>
      <hr />
      <div style={{ display: "flex" }}>
        <div
          style={{
            border: "1px solid grey",
            width: "70%",
            margin: "auto",
          }}
        >
          <input
            style={{
              width: "40%",
              padding: "10px",
              fontSize: "1.2rem",
              marginTop: "30px",
            }}
            placeholder="UserName"
            onChange={(e) => setName(e.target.value)}
          />
          <br />
          <br />
          <input
            style={{ width: "40%", padding: "10px", fontSize: "1.2rem" }}
            placeholder="Caption"
            onChange={(e) => setCap(e.target.value)}
          />
          <br />
          <br />
          <button
            onClick={submit}
            style={{ padding: "10px", fontSize: "1.2rem" }}
          >
            Submit
          </button>
        </div>
      </div>
      <div>
        {post.map((ele, i) => (
          <div key={i} style={{ display: "flex", alignItems: "Center" }}>
            <h2>Name:{ele.name}-</h2>
            <h2>Caption:{ele.cap}-</h2>
            <button>Delete</button>
          </div>
        ))}
      </div>
    </div>
  );
}
