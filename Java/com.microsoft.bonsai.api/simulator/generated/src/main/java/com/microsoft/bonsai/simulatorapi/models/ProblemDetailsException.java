/**
 * Code generated by Microsoft (R) AutoRest Code Generator.
 * Changes may cause incorrect behavior and will be lost if the code is
 * regenerated.
 */

package com.microsoft.bonsai.simulatorapi.models;

import com.microsoft.rest.RestException;
import okhttp3.ResponseBody;
import retrofit2.Response;

/**
 * Exception thrown for an invalid response with ProblemDetails information.
 */
public class ProblemDetailsException extends RestException {
    /**
     * Initializes a new instance of the ProblemDetailsException class.
     *
     * @param message the exception message or the response content if a message is not available
     * @param response the HTTP response
     */
    public ProblemDetailsException(final String message, final Response<ResponseBody> response) {
        super(message, response);
    }

    /**
     * Initializes a new instance of the ProblemDetailsException class.
     *
     * @param message the exception message or the response content if a message is not available
     * @param response the HTTP response
     * @param body the deserialized response body
     */
    public ProblemDetailsException(final String message, final Response<ResponseBody> response, final ProblemDetails body) {
        super(message, response, body);
    }

    @Override
    public ProblemDetails body() {
        return (ProblemDetails) super.body();
    }
}
