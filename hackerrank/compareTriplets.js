function compareTriplets(a, b){
    alice_points = 0
    bob_points = 0

    for (let i = 0; i < a.length; i++) {
        const element = a[i];
        
        if(element > b[i]) {
            alice_points += 1;
        }else if(element < b[i]){
            bob_points += 1;
        }else{
            continue;
        }
    }

    points = [alice_points, bob_points];
    return points
}
a = [17, 28, 30]
b = [99, 16, 8]

console.log(compareTriplets(a, b))