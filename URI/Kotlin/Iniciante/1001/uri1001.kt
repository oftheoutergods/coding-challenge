import java.util.*

fun main(args: Array<String>) {

	val inputlines = Scanner(System.`in`);
	
	val f: String = inputlines.next();
	val s: String = inputlines.next();
	val result = f.toInt() + s.toInt();
	println("X = $result");
}
