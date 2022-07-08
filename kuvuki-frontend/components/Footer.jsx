import React from 'react'
import {AiFillFacebook, AiFillInstagram, AiOutlineTwitter} from "react-icons/ai";


const Footer = () => {
  return (
    <div className="footer-container">
      <p>2022 Kuvuki Headphones All Rights Reserved</p>
        <p className="icons">
            <AiOutlineTwitter />
            <AiFillInstagram />
            <AiFillFacebook />
        </p>
    </div>
  )
}

export default Footer
