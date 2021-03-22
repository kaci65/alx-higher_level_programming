#!/usr/bin/node
// prints text x number of times


const num_int = Number(process.argv[2]);
if (Number.isNaN(num_int))
{
	console.log("Missing number of occurrences");
}
else
{
	let i = 0;
	while (i < num_int)
	{
		console.log("C is fun");
		i++;
	}
}
