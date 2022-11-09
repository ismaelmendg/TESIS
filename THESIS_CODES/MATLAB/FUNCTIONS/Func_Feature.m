%%FEATURE FUNCTION
%DataIn1,DataIn2 and DataIn3 are the data with which the final matrix 
%Rvalue1, Rvalue2 and Rvalue3 are the attempts
% Developed by Ismael Mendoza
% 20/07/2022

function DataOut = Func_Feature(DataIn1,DataIn2,DataIn3, RValue1, RValue2, RValue3)

    DataOut = cat(2,DataIn1,DataIn2,DataIn3);
    DataOut = DataOut';

    x = zeros(length(DataOut)/3, 1);
    x1 = x + RValue1;
    x2 = x + RValue2;
    x3 = x + RValue3;

    x = cat(1, x1, x2, x3);

    DataOut = cat(2, DataOut, x);

end