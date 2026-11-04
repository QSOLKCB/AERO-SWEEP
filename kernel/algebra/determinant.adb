with Interfaces;

package body Determinant with SPARK_Mode => On is

   function In_Bounds (X : Interfaces.Integer_32) return Boolean is
   begin
      return X in Scalar;
   end In_Bounds;

   function Compute_2x2 (A, B, C, D : Scalar) return Exact_Result is
      --  Explicit widening before multiplication.  Every valid input
      --  yields an exact result in [-2_147_352_578, 2_147_352_578].
      Product_AD : constant Exact_Result :=
        Exact_Result (A) * Exact_Result (D);
      Product_BC : constant Exact_Result :=
        Exact_Result (B) * Exact_Result (C);
   begin
      return Product_AD - Product_BC;
   end Compute_2x2;

   function Try_Compute_2x2
     (A, B, C, D : Interfaces.Integer_32) return Computation_Result
   is
   begin
      if In_Bounds (A) and then In_Bounds (B) and then
         In_Bounds (C) and then In_Bounds (D)
      then
         return
           (Status => OK,
            Value => Compute_2x2
              (Scalar (A), Scalar (B), Scalar (C), Scalar (D)));
      else
         return (Status => Invalid_Input, Value => 0);
      end if;
   end Try_Compute_2x2;

end Determinant;
