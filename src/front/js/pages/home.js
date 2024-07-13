import React, { useContext } from "react";
import { Context } from "../store/appContext";

import ShoeCard from "../component/ShoeCard.jsx";

import "../../styles/home.css";

export const Home = () => {
	const { store, actions } = useContext(Context);
  
  const collections = [
		{
			name: "Michael Jordan",
			image: "/path/to/michael-jordan-sneakers.jpg"
		},
		{
			name: "Kobe Bryant",
			image: "/path/to/kobe-bryant-sneakers.jpg"
		},
		{
			name: "LeBron James",
			image: "/path/to/lebron-james-sneakers.jpg"
		},
		{
			name: "Stephen Curry",
			image: "/path/to/stephen-curry-sneakers.jpg"
		},
		{
			name: "Kevin Durant",
			image: "/path/to/kevin-durant-sneakers.jpg"
		}
	];


    return (
        <>
      
        <div>
            {store.shoes.map((shoe) => (
                <ShoeCard key={shoe.id} shoes={shoe} />
            ))}
        </div>

		<div>
			<main>
				<section className="hero">
					<h1>Welcome to Hoop Legend Sneakers</h1>
					<p className="mission-statement">
						At HoopLegendSneakers, we celebrate the legacy of basketball's greatest superstars by bringing you an exclusive collection of iconic sneakers from Michael Jordan, Kobe Bryant, LeBron James, Stephen Curry, and Kevin Durant. Our mission is to connect you with the stories behind each legendary pair, providing not just footwear but a piece of basketball history. With detailed player bios and the rich narratives of their signature sneakers, we aim to inspire and ignite the passion of every basketball enthusiast. Step into greatness and wear the legacy with HoopLegendSneakers.
					</p>
					<a href="/collections" className="explore-button">Explore Collections</a>
				</section>
				<section className="collections">
					{collections.map((collection, index) => (
						<div key={index} className="collection">
							<img src={collection.image} alt={`${collection.name} Sneakers`} />
							<h2>{collection.name}</h2>
						</div>
					))}
				</section>
			</main>
			<footer>
				<p>© 2024 Hoop Legend Sneakers. All rights reserved.</p>
				<ul>
					<li><a href="#">Privacy Policy</a></li>
					<li><a href="#">Terms of Service</a></li>
				</ul>
			</footer>
		</div>
	);
  </>
};
