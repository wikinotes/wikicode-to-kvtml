import java.io.*;
import java.util.Scanner;

public class ConvertToQuiz {
	public static void main(String[] args) {
		System.out.print("Input filename: ");
		Scanner keyboard = new Scanner(System.in);
		String inputFilename = keyboard.nextLine();
		File inputFile = new File(inputFilename);
		String outputFilename = inputFilename + ".kvtml";
		
		// WTF WHY ARE YOU SUCH A SHIT COMMENTER
		if ( args.length > 0 ) {
			// then do options
			if ( args[0].equals("lowercase") ) {
				try {
					convertToLowercase(inputFile);
					System.out.println("Successful, check " + inputFilename);
				} catch (IOException e) {
					System.err.println("lol lowercase");
				}
			}
		} else {	
			try {
				readFile(inputFile, outputFilename);
				System.out.println("Successful, check " + outputFilename);
			} catch (IOException e) {
				System.err.println("lol");
			}
		}
	}
	
	public static void convertToLowercase(File file) throws IOException {
		Scanner input = new Scanner(file);
		//FUCK IT
		
	}
	
	public static void readFile(File file, String output) throws IOException {
	
		Scanner input = new Scanner(file);
		PrintWriter out = new PrintWriter(output);
		String thisLine;
		String term, definition;
		int separator;
		int id = 0;
		
		out.print("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE kvtml PUBLIC \"kvtml2.dtd\" \"http://edu.kde.org/kvtml/kvtml2.dtd\">\n<kvtml version=\"2.0\">\n\t<information>\n\t\t<generator>kwordquiz 0.9.1</generator>\n\t\t<title>BIOL 111 Vocab</title>\n\t\t<date>2010-12-14</date>\n\t</information>\n\t<identifiers>\n\t\t<identifier id=\"0\">\n\t\t\t<name>Term</name>\n\t\t\t<locale>Term</locale>\n\t\t</identifier>\n\t\t<identifier id=\"1\">\n\t\t\t<name>Definition</name>\n\t\t\t<locale>Definition</locale>\n\t\t</identifier>\n\t</identifiers>\n\n\t<entries>");
		
		while ( input.hasNextLine() ) {
			thisLine = input.nextLine();
			separator = thisLine.indexOf("@");
			//System.out.println("" + separator + " " + id);
			term = thisLine.substring(0, separator);
			definition = thisLine.substring(separator + 1); //until the end
			out.print("\n\t\t<entry id=\"" + id + "\">\n\t\t\t<translation id=\"0\">\n\t\t\t\t<text>");
			out.print(term);
			out.print("</text>\n\t\t\t</translation>");
			out.print("\n\t\t\t<translation id=\"1\">\n\t\t\t\t<text>");
			out.print(definition);
			out.print("</text>\n\t\t\t</translation>");
			out.print("\n\t\t</entry>");
    			id++;
    			// bitch comment better next time
		}
		
		out.print("\n\t</entries>\n\n</kvtml>");
		out.close();
	}
}
