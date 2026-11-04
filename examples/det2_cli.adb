with Ada.Command_Line;
with Ada.Strings;
with Ada.Strings.Fixed;
with Ada.Text_IO;
with Determinant;
with Interfaces;

--  CLI integration surface for AS-001 testing only; NOT the C ABI.
--  Usage: det2_cli a b c d
--  Output: OK <integer> | INVALID_INPUT 0 | PARSE_ERROR 0
procedure Det2_CLI is
   use Ada.Command_Line;
   use Ada.Text_IO;

   type Input_Array is array (Positive range 1 .. 4)
     of Interfaces.Integer_32;
   Inputs : Input_Array := (others => 0);
begin
   if Argument_Count /= 4 then
      Put_Line ("PARSE_ERROR 0");
      Set_Exit_Status (Failure);
      return;
   end if;

   for I in Inputs'Range loop
      begin
         Inputs (I) := Interfaces.Integer_32'Value (Argument (I));
      exception
         when Constraint_Error =>
            Put_Line ("PARSE_ERROR 0");
            Set_Exit_Status (Failure);
            return;
      end;
   end loop;

   declare
      Answer : constant Determinant.Computation_Result :=
        Determinant.Try_Compute_2x2
          (Inputs (1), Inputs (2), Inputs (3), Inputs (4));
   begin
      case Answer.Status is
         when Determinant.OK =>
            Put_Line
              ("OK " & Ada.Strings.Fixed.Trim
                 (Determinant.Exact_Result'Image (Answer.Value),
                  Ada.Strings.Both));
         when Determinant.Invalid_Input =>
            Put_Line ("INVALID_INPUT 0");
      end case;
   end;
end Det2_CLI;
