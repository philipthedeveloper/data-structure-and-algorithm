const formData = new FormData();
formData.append("name", "John");
formData.append("age", 14);

// const parseFormDataSynchronously = (formData) => {
//   let parsedData = {};

//   // Use FormData.get() to access values by key
//   formData.forEach((value, key) => {
//     if (key !== "files") {
//       // Don't store files since they have not been uploaded
//       if (!parsedData[key]) {
//         // If the key is not already present, add it to the parsedData
//         parsedData[key] = value;
//       }
//     }
//   });

//   return parsedData;
// };

const parseFormDataSynchronously = (formData) => {
  let parsedData = {};
  for (let [key, value] of formData.entries()) {
    if (key !== "files") {
      // Don't store files since they have not been uploaded
      if (!parsedData[key]) {
        // If the key is not already present add it to the parseData
        // By default this is the expected behavior because only files have mulitple values
        parsedData[key] = value;
      }
    }
  }
  return parsedData;
};

console.log(parseFormDataSynchronously(formData));
