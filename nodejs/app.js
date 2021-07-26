const express = require("express");

// Assigning directory to respective var names
const videoInfoRoutes = require("./routes/videoInfo");
const hashtagInfoRoutes = require("./routes/hashtagInfo");

require("dotenv").config();
const app = express();
const cors = require("cors");

// allow for parsing of req body
app.use(express.json({ limit: "20mb" }));

app.get("/", (req, res) => res.send("Hello world!"));
app.use("/video", videoInfoRoutes);
app.use("/hashtag", hashtagInfoRoutes);

const PORT = 4000;

app.use(cors());

app.listen(PORT, function () {
  console.warn("Server is running on Port: " + PORT);
});

module.exports = { app };
