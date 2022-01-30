fn main() {
let rect1 = (35,55);

    println!("The area of the rectangle is {} square pixels.", area(rect1));
}
fn area(dimensions:(u32,u32))-> u32 {
    dimensions.0 * dimensions.1
}