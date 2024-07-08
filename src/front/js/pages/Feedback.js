import React, { useState } from "react";

export const Feedback = () => {
    const [feedbackText, setFeedbackText] = useState(""); 
    const maxCharacters = 300; 

    const handleChange = (event) => {
        setFeedbackText(event.target.value); 
    };

    const charactersLeft = maxCharacters - feedbackText.length;

    return (
        <>
            <nav className="navbar fixed-bottom bg-body-tertiary bg-dark">
                <div className="container-fluid">
                    <a className="navbar-brand">About Us</a>
                    <a className="navbar-brand">Contact Us</a>
                    <a className="navbar-brand">Privacy Policy</a>
                    <a className="navbar-brand" data-bs-toggle="modal" data-bs-target="#staticBackdrop" >Feedback</a>
                </div>
            </nav>

            <div className="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabIndex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
                <div className="modal-dialog">
                    <div className="modal-content">
                        <div className="modal-header">
                            <h1 className="modal-title fs-5" id="staticBackdropLabel">Feedback</h1>
                            <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div className="modal-body">
                            <div class="mb-3">
                                <label for="exampleFormControlTextarea1" class="form-label">Enter your feedback</label>
                                <textarea
                                    className="form-control"
                                    id="exampleFormControlTextarea1"
                                    rows="3"
                                    value={feedbackText}
                                    onChange={handleChange} 
                                >
                                </textarea>
                                <small className="text-muted">{charactersLeft} characters left</small>
                            </div>
                        </div>
                        <div className="modal-footer">
                            <button type="button" className="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            <button type="button" className="btn btn-primary" data-bs-dismiss="modal">Submit</button>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
};

export default Feedback;