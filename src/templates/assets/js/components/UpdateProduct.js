import React, { useState, useEffect } from "react";
import axios from "axios";
import TagsInput from "react-tagsinput";
import "react-tagsinput/react-tagsinput.css";
import Dropzone from "react-dropzone";

const UpdateProduct = (props) => {
  const [title, setTitle] = useState("");
  const [sku, setSku] = useState("");
  const [description, setDescription] = useState("");
  const [productVariants, setProductVariant] = useState([
    {
      option: 1,
      tags: [],
    },
  ]);

  useEffect(()=>{
    axios({
      method: "get",
      url: "http://localhost:8000/api/product/"+ props.product_id
    }).then((res)=>{
      const data = res.data
      const product = data.data
      setTitle(product.title)
      setSku(product.sku)
      setDescription(product.description)

    })

  },[])
 

  // console.log(appState.productVariants)
  // console.log(appState.productVariants)


  // const [title, setTitle] = useState("");
  // const [sku, setSku] = useState("");
  // const [description, setDescription] = useState("");
  // const [productVariantPrices, setProductVariantPrices] = useState([]);
  // const [productVariants, setProductVariant] = useState([
  //   {
  //     option: 1,
  //     tags: [],
  //   },
  // ]);

  // // To get csrf token
  // function getCookie(name) {
  //   let cookieValue = null;
  //   if (document.cookie && document.cookie !== "") {
  //     const cookies = document.cookie.split(";");
  //     for (let i = 0; i < cookies.length; i++) {
  //       const cookie = cookies[i].trim();
  //       if (cookie.substring(0, name.length + 1) === name + "=") {
  //         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
  //         break;
  //       }
  //     }
  //   }
  //   return cookieValue;
  // }

  // // handle click event of the Add button
  // const handleAddClick = () => {
  //   let all_variants = JSON.parse(props.variants.replaceAll("'", '"')).map(
  //     (el) => el.id
  //   );
  //   let selected_variants = productVariants.map((el) => el.option);
  //   let available_variants = all_variants.filter(
  //     (entry1) => !selected_variants.some((entry2) => entry1 == entry2)
  //   );
  //   setProductVariant([
  //     ...productVariants,
  //     {
  //       option: available_variants[0],
  //       tags: [],
  //     },
  //   ]);
  // };

  // // handle input change on tag input
  // const handleInputTagOnChange = (value, index) => {
  //   let product_variants = [...productVariants];
  //   product_variants[index].tags = value;
  //   setProductVariant(product_variants);

  //   checkVariant();
  // };

  // // remove product variant
  // const removeProductVariant = (index) => {
  //   let product_variants = [...productVariants];
  //   product_variants.splice(index, 1);
  //   setProductVariant(product_variants);
  // };

  // // check the variant and render all the combination
  // const checkVariant = () => {
  //   let tags = [];

  //   productVariants.filter((item) => {
  //     tags.push(item.tags);
  //   });

  //   setProductVariantPrices([]);

  //   getCombn(tags).forEach((item) => {
  //     setProductVariantPrices((productVariantPrice) => [
  //       ...productVariantPrice,
  //       {
  //         title: item,
  //         price: 0,
  //         stock: 0,
  //       },
  //     ]);
  //   });
  // };

  // // combination algorithm
  // function getCombn(arr, pre) {
  //   pre = pre || "";
  //   if (!arr.length) {
  //     return pre;
  //   }
  //   let ans = arr[0].reduce(function (ans, value) {
  //     return ans.concat(getCombn(arr.slice(1), pre + value + "/"));
  //   }, []);
  //   return ans;
  // }

  // const handleProductVariantPrice = (e) =>{
  //   var index = e.target.getAttribute('data-index')
  //   var productVariantPrice = productVariantPrices[index]

  //   if(e.target.name == 'price'){
  //     productVariantPrice.price = e.target.value
  //   }else if(e.target.name == 'stock'){
  //     productVariantPrice.stock = e.target.value
  //   }
  // }
  // // Save product
  // let saveProduct = (event) => {
  //   event.preventDefault();
  //   const csrftoken = getCookie("csrftoken");
  //   // TODO : write your code here to save the product
  //   let formField = new FormData();

  //   formField.append("title", title);
  //   formField.append("sku", sku);
  //   formField.append("description", description);
  //   var product = {
  //     title: title,
  //     sku: sku,
  //     description: description,
  //   };

  //   axios({
  //     method: "post",
  //     headers: { "X-CSRFToken": csrftoken },
  //     url: "http://localhost:8000/api/product/",
  //     data: {
  //       product: product,
  //       productVariants: productVariants,
  //       productVariantPrices: productVariantPrices,
  //     },
  //   }).then((res) => {
  //     console.log(res.data);
  //   });
  // };

  return (
    <div>
      <section>
        <div className="row">
          <div className="col-md-6">
            <div className="card shadow mb-4">
              <div className="card-body">
                <div className="form-group">
                  <label htmlFor="">Product Name</label>
                  <input
                    type="text"
                    placeholder="Product Name"
                    className="form-control"
                    name="title"
                    defaultValue={title}
                    onChange={(e) => setTitle(e.target.value)}
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="">Product SKU</label>
                  <input
                    type="text"
                    placeholder="Product Sku"
                    className="form-control"
                    name="sku"
                    defaultValue={sku}
                    onChange={(e) => setSku(e.target.value)}
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="">Description</label>
                  <textarea
                    id=""
                    cols="30"
                    rows="4"
                    className="form-control"
                    name="description"
                    defaultValue={description}
                    onChange={(e) => setDescription(e.target.value)}
                  ></textarea>
                </div>
              </div>
            </div>

            <div className="card shadow mb-4">
              <div className="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                <h6 className="m-0 font-weight-bold text-primary">Media</h6>
              </div>
              <div className="card-body border">
                <Dropzone
                  onDrop={(acceptedFiles) => console.log(acceptedFiles)}
                >
                  {({ getRootProps, getInputProps }) => (
                    <section>
                      <div {...getRootProps()}>
                        <input {...getInputProps()} />
                        <p>
                          Drag 'n' drop some files here, or click to select
                          files
                        </p>
                      </div>
                    </section>
                  )}
                </Dropzone>
              </div>
            </div>
          </div>

          {/* <div className="col-md-6">
            <div className="card shadow mb-4">
              <div className="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                <h6 className="m-0 font-weight-bold text-primary">Variants</h6>
              </div>
              <div className="card-body">
                {productVariants.map((element, index) => {
                  return (
                    <div className="row" key={index}>
                      <div className="col-md-4">
                        <div className="form-group">
                          <label htmlFor="">Option</label>
                          <select
                            className="form-control"
                            defaultValue={element.option}
                          >
                            {JSON.parse(
                              props.variants.replaceAll("'", '"')
                            ).map((variant, index) => {
                              return (
                                <option key={index} value={variant.id}>
                                  {variant.title}
                                </option>
                              );
                            })}
                          </select>
                        </div>
                      </div>

                      <div className="col-md-8">
                        <div className="form-group">
                          {productVariants.length > 1 ? (
                            <label
                              htmlFor=""
                              className="float-right text-primary"
                              style={{ marginTop: "-30px" }}
                              onClick={() => removeProductVariant(index)}
                            >
                              remove
                            </label>
                          ) : (
                            ""
                          )}

                          <section style={{ marginTop: "30px" }}>
                            <TagsInput
                              value={element.tags}
                              style="margin-top:30px"
                              onChange={(value) =>
                                handleInputTagOnChange(value, index)
                              }
                            />
                          </section>
                        </div>
                      </div>
                    </div>
                  );
                })}
              </div>
              <div className="card-footer">
                {productVariants.length !== 3 ? (
                  <button className="btn btn-primary" onClick={handleAddClick}>
                    Add another option
                  </button>
                ) : (
                  ""
                )}
              </div>

              <div className="card-header text-uppercase">Preview</div>
              <div className="card-body">
                <div className="table-responsive">
                  <table className="table">
                    <thead>
                      <tr>
                        <td>Variant</td>
                        <td>Price</td>
                        <td>Stock</td>
                      </tr>
                    </thead>
                    <tbody>
                      {productVariantPrices.map(
                        (productVariantPrice, index) => {
                          return (
                            <tr key={index}>
                              <td>{productVariantPrice.title}</td>
                              <td>
                                <input 
                                  className="form-control" 
                                  type="text" 
                                  name="price"
                                  data-index={index}
                                  onChange={handleProductVariantPrice}
                                />
                              </td>
                              <td>
                                <input 
                                className="form-control" 
                                type="text"
                                name="stock" 
                                data-index={index}
                                onChange={handleProductVariantPrice}
                                />
                              </td>
                            </tr>
                          );
                        }
                      )}
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div> */}
        </div>

        <button
          type="button"
          // onClick={saveProduct}
          className="btn btn-lg btn-primary"
        >
          Save
        </button>
        <button type="button" className="btn btn-secondary btn-lg">
          Cancel
        </button>
      </section>
    </div>
  );
};

export default UpdateProduct;
