with Interfaces;

--  AS-001: headless, bounded, exact 2x2 determinant.
--  This is an Ada-only API, NOT the proposed C ABI (AS-003).
package Determinant with SPARK_Mode => On is
   subtype Scalar is Interfaces.Integer_32 range -32_767 .. 32_767;
   subtype Exact_Result is Interfaces.Integer_64;

   type Computation_Status is (OK, Invalid_Input);

   type Computation_Result is record
      Status : Computation_Status;
      Value  : Exact_Result;
   end record;

   function In_Bounds (X : Interfaces.Integer_32) return Boolean
     with Global => null,
          Post => In_Bounds'Result = (X in Scalar);

   --  Rows are (A, B) and (C, D).  DO NOT substitute A*B - C*D.
   function Compute_2x2 (A, B, C, D : Scalar) return Exact_Result
     with Global => null,
          Post => Compute_2x2'Result =
            Exact_Result (A) * Exact_Result (D) -
            Exact_Result (B) * Exact_Result (C);

   --  Total for any four signed 32-bit inputs; never call the bounded
   --  function with out-of-domain values.
   function Try_Compute_2x2
     (A, B, C, D : Interfaces.Integer_32) return Computation_Result
     with Global => null,
          Post =>
            (if A in Scalar and then B in Scalar and then
                C in Scalar and then D in Scalar
             then
               Try_Compute_2x2'Result.Status = OK and then
               Try_Compute_2x2'Result.Value =
                 Exact_Result (A) * Exact_Result (D) -
                 Exact_Result (B) * Exact_Result (C)
             else
               Try_Compute_2x2'Result.Status = Invalid_Input and then
               Try_Compute_2x2'Result.Value = 0);
end Determinant;
