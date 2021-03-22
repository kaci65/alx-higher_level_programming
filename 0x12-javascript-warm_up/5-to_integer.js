#!/usr/bin/node
// print text if argument can be converted to int


const num_int = Number(process.argv[2]);
if (Number.isNaN(num_int))
{
	console.log("Not a number");
}
else
{
	console.log("My number: " + num_int);
}
