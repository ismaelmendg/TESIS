%%NORMALIZED MATRIX FUNCTION
%DataIn - Matrix to normalize
% Developed by Ismael Mendoza
% 20/07/2022

function DataOut = Func_Nor(DataIn)

    DataOut = DataIn/max(DataIn,[],'all');
    
end