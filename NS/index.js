const audioIN = { audio: true };

navigator.mediaDevices
  .getUserMedia(audioIN)
  .then(mediaStreamObj => {
    const micro = document.getElementById("micro");
    const file = document.querySelector("#file");
    const form = document.querySelector("form");
    const container = document.querySelector(".container");

    const mediaRecorder = new MediaRecorder(mediaStreamObj);

    const start = () => {
      mediaRecorder.start();
      container.classList.add("active");
    };

    const end = () => {
      mediaRecorder.stop();

      setTimeout(() => {
        container.classList.remove("active");
      }, 1000);
    };

    micro.addEventListener("mousedown", start);
    micro.addEventListener("touchstart", start);

    micro.addEventListener("mouseup", end);
    micro.addEventListener("touchend", end);

    mediaRecorder.ondataavailable = ev => {
      dataArray.push(ev.data);
    };

    let dataArray = [];

    form.addEventListener("submit", e => {
      e.preventDefault();
    });

    mediaRecorder.onstop = async ev => {
      const audioData = new Blob(dataArray, {
        type: "audio/wav",
      });
      dataArray = [];

      const formData = new FormData();
      formData.append("file", audioData);

      await fetch("http://127.0.0.1:5500/upload", {
        method: "POST",
        body: formData
      });
    };
  })
  .catch(function (err) {
    console.log(err.name, err.message);
  });
