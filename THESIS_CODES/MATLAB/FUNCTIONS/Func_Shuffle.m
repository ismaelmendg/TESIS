%%RANDOM FUNCTION FOR MATRIX
% Array to which the random will be applied
% Developed by Ismael Mendoza
% 20/07/2022

function DataOut = Func_Shuffle(DataIn)

    DataOut = DataIn(randperm(size(DataIn,1)),:);

end