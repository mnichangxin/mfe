<!--  canva 面试 -->
<script>
  console.log("hello");

  function dummyFetch(url) {
    return new Promise((resolve) => {
      setTimeout(() => resolve(`dummy data for ${url}`), Math.random() * 4000);
    });
  }

  //   const urls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  //   //   let counter = 0;
  //   let accumulator = [];
  //   const result = urls.map((url) => {
  //     this.dummyFetch(url).then((data) => {
  //       //   console.log("I got", data);
  //       //   counter += 1;
  //       accumulator.push(data);
  //       //   if (counter === 10) {
  //   //       //     console.log(accumulator);
  //   //       //   }
  //   //     });
  //       return this.dummyFetch(url);
  //     });

  //     console.log(counter);

  function fetchDesign(designId) {
    return new Promise((resolve) => {
      setTimeout(
        () =>
          resolve({
            shapes: [
              {
                shapeId: "basic-shape",
                color: { r: 55, g: 40, b: 255 },
                children: [],
              },
              {
                shapeId: "person",
                color: { r: 255, g: 255, b: 252 },
                children: [
                  {
                    shapeId: "person-head",
                    color: { r: 255, g: 255, b: 255 },
                    children: [],
                  },
                  {
                    shapeId: "person-body",
                    color: { r: 205, g: 255, b: 252 },
                    children: [],
                  },
                  {
                    shapeId: "person-legs",
                    color: { r: 100, g: 255, b: 252 },
                    children: [],
                  },
                ],
              },
              {
                shapeId: "zigzag-polygon",
                color: { r: 205, g: 255, b: 252 },
                children: [],
              },
              {
                shapeId: "fish",
                color: { r: 205, g: 255, b: 252 },
                children: [
                  {
                    shapeId: "fish-eyes",
                    color: { r: 255, g: 255, b: 255 },
                    children: [],
                  },
                  {
                    shapeId: "fish-fin",
                    color: { r: 100, g: 66, b: 74 },
                    children: [
                      {
                        shapeId: "fish-fin-part-1",
                        color: { r: 93, g: 54, b: 55 },
                        children: [],
                      },
                      {
                        shapeId: "fish-fin-part-2",
                        color: { r: 33, g: 255, b: 255 },
                        children: [],
                      },
                      {
                        shapeId: "fish-fin-part-3",
                        color: { r: 128, g: 53, b: 255 },
                        children: [],
                      },
                    ],
                  },
                  {
                    shapeId: "fish-tail",
                    color: { r: 255, g: 5, b: 255 },
                    children: [],
                  },
                ],
              },
              {
                shapeId: "person",
                color: { r: 255, g: 255, b: 252 },
                children: [
                  {
                    shapeId: "person-head",
                    color: { r: 255, g: 255, b: 255 },
                    children: [],
                  },
                  {
                    shapeId: "person-body",
                    color: { r: 205, g: 255, b: 252 },
                    children: [],
                  },
                  {
                    shapeId: "person-legs",
                    color: { r: 100, g: 255, b: 252 },
                    children: [],
                  },
                ],
              },
            ],
          }),
        Math.random() * 1000,
      );
    });
  }

  const urls = [1];
  //   let counter = 0;

  function extractColor(shapes, accumulator) {
    let colors = shapes.map((shape) => shape["color"]);
    let children = shapes.map((shape) => shape["children"]);
    console.log("colors", colors);
    console.log("childern", children);
    children.forEach((child) => {
      if (child !== []) {
        this.extractColor(child, accumulator);
      }
    });
    let result = colors.reduce((acc, color) => {
      //   console.log(color);
      ["r", "g", "b"].forEach((element) => {
        if (element in acc) {
          acc[element] += color[element];
        } else {
          acc[element] = color[element];
        }
      });
      acc.count += 1;
      return acc;
    }, accumulator);
    console.log("result", result);
    return result;
  }

  let accumulator = [];
  const result = urls.map((url) => {
    this.fetchDesign(url).then((data) => {
      //   console.log("I got", data);
      //   counter += 1;
      let shapes = data["shapes"];
      let color_sum = this.extractColor(shapes, {});

      let obj = {};
      ["r", "g", "b"].forEach((element) => {
        obj[element] = result[element] / data["shapes"].length;
      });
      console.log("Design ", url, ": ", obj);
    });
    // console.log(accumulator);
  });
</script>
