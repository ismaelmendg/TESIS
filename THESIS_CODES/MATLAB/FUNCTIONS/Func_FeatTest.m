%%FEATURE FUNCTION TEST
%DataIn - percentage of data for feature test
% Developed by Ismael Mendoza
% 20/07/2022

function DataOut = Func_FeatTest(DataIn)

    DataOut = DataIn((length( DataIn)*.8)+1:end,:);

end