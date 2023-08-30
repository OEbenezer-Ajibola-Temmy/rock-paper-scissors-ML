# Flask Server Documentation

## Overview

This documentation provides an overview of the Flask server API, specifically focusing on the `/predict` endpoint. The `/predict` endpoint is designed to receive three images encoded as base64 strings in a JSON object. The server processes the images and returns a JSON response containing the prediction result.

## Endpoint Details

### Endpoint: `/predict`
- Method: POST
- URL: https://rock-paperscissors.azurewebsites.net/predict
- Input: JSON object containing three images encoded as base64 strings
- Output: JSON response containing the prediction result or an error message

## Request Format

The `/predict` endpoint expects a JSON object with the following structure:

```json
{
  "images": [
    "base64_string_image1",
    "base64_string_image2",
    "base64_string_image3"
  ]
}
```

- `images`: A list of three base64-encoded image strings.

## Response Format

The server's response will be in the following JSON format:

```json
{
  "result": "prediction_result"
}
```

- `result`: A string containing the prediction result, which can be one of the following values: "Rock", "Paper", "Scissors", "No image".

## Error Handling

If the server encounters an issue during processing or if the input data is not in the expected format, it will respond with an error message. The error response will have the following format:

```json
{
  "error": "error_message"
}
```

- `error`: A string describing the error that occurred.

## Handling "No Image" Response

When the server responds with a prediction result of "No image", it indicates that there was an issue with the input images. This response should be properly handled on the frontend to provide appropriate feedback to the user. For instance, you can display an error message or a notification indicating that the images were not processed successfully.

## Example Usage

### Request

```json
POST /predict
Content-Type: application/json

{
  "images": [
    "base64_string_image1",
    "base64_string_image2",
    "base64_string_image3"
  ]
}
```

### Successful Response

```json
HTTP/1.1 200 OK
Content-Type: application/json

{
  "result": "Rock"
}
```

### Error Response

```json
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
  "error": "Invalid input data"
}
```

## Conclusion

The `/predict` endpoint of the Flask server is designed to receive three images as base64 strings and provide a prediction result based on the processed images. Proper handling of responses, including the "No image" case, is essential to ensure a smooth user experience on the frontend.
