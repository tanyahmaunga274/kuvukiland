import React from "react";
import Link from "next/link";
import Image from 'next/image'

const HeroBanner = ({ heroBanner }) => {
  return (
    <div className="hero-banner-container">
      <p className="beats-solo">{heroBanner.smallText}</p>
      <h3>{heroBanner.midText}</h3>
      <h1>{heroBanner.largeText1}</h1>
      <Image src="" alt="headphones" className="hero-banner-image" />
      <div>
        <Link href={`product/${heroBanner.product}`}>
          <button type="button">{heroBanner.buttonText}</button>
        </Link>
        <div className="desc">
          <h5>DESCRIPTION</h5>
          <p>HERO BANNER DESCRIPTION</p>
        </div>
      </div>
    </div>
  );
};

export default HeroBanner;
