#eventloop

event loop, which handles the execution of multiple chunks of your program over time, each time invoking the JS Engine.

this is how concurrency works in JS
basically pushes out all the cb function out of stack(to task(cb) queue once they are done).. and add it back once they are done ..


console.log('hi');
setTimeout( () => {
    console.log('time out ');
},0)
console.log('hi2');