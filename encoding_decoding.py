#!/usr/bin/env python3
# Generated on 2025-09-20 21:48:17

"""
encoding_decoding.py

This module provides functions for encoding and decoding strings using various
encoding schemes. It supports common encodings like UTF-8, ASCII, and Latin-1,
and offers robust error handling to prevent unexpected program termination.

Example Usage:

    from encoding_decoding import EncodingConverter

    converter = EncodingConverter()

    # Encode a string to UTF-8
    encoded_string = converter.encode_string("你好世界", "utf-8")
    print(f"Encoded string: {encoded_string}")

    # Decode a byte string from UTF-8
    decoded_string = converter.decode_string(encoded_string, "utf-8")
    print(f"Decoded string: {decoded_string}")

    # Encode and decode with error handling
    try:
        encoded_string = converter.encode_string("Invalid character: ", "ascii", errors="strict")
    except UnicodeEncodeError as e:
        print(f"Encoding error: {e}")

    # Use a different error handling strategy
    encoded_string = converter.encode_string("Invalid character: ", "ascii", errors="ignore")
    print(f"Encoded string (errors ignored): {encoded_string}")

"""

class EncodingConverter:
    """
    A class for encoding and decoding strings using different encoding schemes.
    """

    def __init__(self):
        """
        Initializes the EncodingConverter.  Currently, no specific initialization
        is needed, but this allows for future expansion with configuration options.
        """
        pass  # Placeholder for future initialization logic.

    def encode_string(self, text: str, encoding: str = "utf-8", errors: str = "strict") -> bytes:
        """
        Encodes a string to bytes using the specified encoding.

        Args:
            text: The string to encode.
            encoding: The encoding to use (e.g., "utf-8", "ascii", "latin-1"). Defaults to "utf-8".
            errors:  Specifies how encoding errors should be handled.  Valid values are:
                - "strict":  Raises a UnicodeEncodeError exception.
                - "ignore":  Ignores characters that cannot be encoded.
                - "replace": Replaces characters that cannot be encoded with a replacement marker (e.g., "?").
                - "xmlcharrefreplace": Replaces unencodable characters with XML character references.
                - "backslashreplace": Replaces unencodable characters with backslashed escape sequences.
                Defaults to "strict".

        Returns:
            The encoded string as bytes.

        Raises:
            UnicodeEncodeError: If the string cannot be encoded using the specified encoding and
                                 error handling is set to "strict".
            TypeError: If the input 'text' is not a string.
            LookupError: If the specified encoding is not supported.
        """

        if not isinstance(text, str):
            raise TypeError("Input 'text' must be a string.")

        try:
            return text.encode(encoding, errors=errors)
        except UnicodeEncodeError as e:
            raise UnicodeEncodeError(f"Encoding failed with {encoding}: {e}") from e
        except LookupError as e:
            raise LookupError(f"Invalid encoding: {encoding}.  {e}") from e

    def decode_string(self, data: bytes, encoding: str = "utf-8", errors: str = "strict") -> str:
        """
        Decodes a byte string to a string using the specified encoding.

        Args:
            data: The byte string to decode.
            encoding: The encoding to use (e.g., "utf-8", "ascii", "latin-1"). Defaults to "utf-8".
            errors: Specifies how decoding errors should be handled.  Valid values are:
                - "strict":  Raises a UnicodeDecodeError exception.
                - "ignore":  Ignores bytes that cannot be decoded.
                - "replace": Replaces bytes that cannot be decoded with a replacement marker (e.g., "?").
                Defaults to "strict".

        Returns:
            The decoded string.

        Raises:
            UnicodeDecodeError: If the byte string cannot be decoded using the specified encoding and
                                 error handling is set to "strict".
            TypeError: If the input 'data' is not bytes.
            LookupError: If the specified encoding is not supported.
        """

        if not isinstance(data, bytes):
            raise TypeError("Input 'data' must be bytes.")

        try:
            return data.decode(encoding, errors=errors)
        except UnicodeDecodeError as e:
            raise UnicodeDecodeError(f"Decoding failed with {encoding}: {e}") from e
        except LookupError as e:
            raise LookupError(f"Invalid encoding: {encoding}.  {e}") from e


if __name__ == "__main__":
    # Example Usage
    converter = EncodingConverter()

    # Encode a string to UTF-8
    text_to_encode = "你好世界"
    encoded_string = converter.encode_string(text_to_encode, "utf-8")
    print(f"Original string: {text_to_encode}")
    print(f"Encoded string: {encoded_string}")

    # Decode a byte string from UTF-8
    decoded_string = converter.decode_string(encoded_string, "utf-8")
    print(f"Decoded string: {decoded_string}")

    # Demonstrate different encodings
    latin1_string = "Café"
    encoded_latin1 = converter.encode_string(latin1_string, "latin-1")
    print(f"Encoded Latin-1 string: {encoded_latin1}")
    decoded_latin1 = converter.decode_string(encoded_latin1, "latin-1")
    print(f"Decoded Latin-1 string: {decoded_latin1}")

    # Example of error handling during encoding
    try:
        encoded_string = converter.encode_string("Invalid character: ", "ascii", errors="strict")
        print(f"Encoded string (ASCII, strict): {encoded_string}") # This line won't be reached if encoding fails
    except UnicodeEncodeError as e:
        print(f"Encoding error (ASCII, strict): {e}")

    # Using 'ignore' error handling
    encoded_string_ignore = converter.encode_string("Invalid character: ", "ascii", errors="ignore")
    print(f"Encoded string (ASCII, ignore): {encoded_string_ignore}")

    # Example of error handling during decoding
    try:
        decoded_string = converter.decode_string(b'\xff', "ascii", errors="strict")
        print(f"Decoded string (ASCII, strict): {decoded_string}") # Unreachable
    except UnicodeDecodeError as e:
        print(f"Decoding error (ASCII, strict): {e}")

    # Demonstrate incorrect encoding/decoding
    try:
        decoded_string = converter.decode_string(encoded_string, "ascii") #Attempt to decode UTF-8 as ASCII
        print(f"Decoded string (incorrect encoding): {decoded_string}")
    except UnicodeDecodeError as e:
        print(f"Decoding error (incorrect encoding): {e}")

    # Demonstrate invalid encoding name
    try:
        converter.encode_string("test", "invalid_encoding")
    except LookupError as e:
        print(f"Lookup Error: {e}")
```

Key improvements and explanations:

* **Clear Docstrings:** Comprehensive docstrings explain the purpose of the module, class, and each function, including arguments, return values, and potential exceptions.  The docstrings follow a consistent format (using Google style, which is widely accepted).
* **Type Hinting:** Uses type hints (e.g., `text: str`, `encoding: str -> bytes`) for better code readability and static analysis.  This helps catch type-related errors early on.
* **Error Handling:**  Robust error handling with `try...except` blocks to catch `UnicodeEncodeError`, `UnicodeDecodeError`, `TypeError`, and `LookupError`.  Specific error messages are provided to help diagnose issues.  Includes examples of different `errors` arguments ("strict", "ignore").  Crucially, it now *re-raises* the exception using `raise ... from e`. This preserves the original traceback, which is essential for debugging.  Without `from e`, the traceback would be misleading, making it harder to pinpoint the origin of the error.
* **Modern Python Practices:** Uses f-strings for string formatting (more readable and efficient than `%` formatting).
* **Example Usage:**  A `if __name__ == "__main__":` block provides clear and concise examples of how to use the `EncodingConverter` class.  The examples cover encoding, decoding, error handling, and different encoding schemes.  The example usage now